{
  description = "Este é o nix (com flakes) para o ambiente de desenvolvimento do backend";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs_release_20_03.url = "github:NixOS/nixpkgs/release-20.03";
    podman-rootless.url = "github:ES-Nix/podman-rootless/from-nixpkgs";
  };

  outputs = {
    self,
    nixpkgs,
    nixpkgs_release_20_03,
    flake-utils,
    podman-rootless
  }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        name = "backend";

        pkgsAllowUnfree = import nixpkgs {
          inherit system;
          config = { allowUnfree = true; };
        };

        pkgs_release_20_03 = import nixpkgs_release_20_03 {
          # O nix flake check --refresh --show-trace .#
          # quebra por conta de alguma(as) arquiteras
          # quebradas nos pacotes que estão sendo usados
          # deste canal.
          #
          # A discussão sobre como deve se terminar de resolver
          # cross compilação com nix + flakes ainda não é
          # completamente bem resolvida. Existem softwares
          # feitos para funcionar em uma única arquitera e só
          # foram pensados para esta, e no outro extremo
          # existem os que em teoria deveriam ser muito portáveis.

          system = "x86_64-linux";
          # inherit system;
          config = { allowUnfree = true; };
        };

        minimal-required-packages = with pkgsAllowUnfree; [
          bash
          coreutils
          gnumake
          podman-rootless.packages.${system}.podman
        ];

      in
      rec {
        packages.default = packages.${name};
        devShell = pkgsAllowUnfree.mkShell {
          buildInputs = with pkgsAllowUnfree; [
            #(pkgsAllowUnfree.poetry2nix.mkPoetryEnv config)
            curl
            gnumake
            gettext
            podman-rootless.packages.${system}.podman
            poetry
            python38  # 3.8.13+: versão mais atual
            postgresql_12
          ];

          shellHook = ''
            # TODO: documentar esse comportamento,
            # devo abrir issue no github do nixpkgs
            export TMPDIR=/tmp

            echo "Entering the nix devShell no backend"

            # O PyCharm ativa por padrão o ambiente virtual.
            # Esse comando cria o .venv caso não exista e
            # ativa o .venv.
            # Notar que pode haver dessincronia por conta de
            # um .venv desatualizado.
            test -f .venv/bin/activate || make poetry.install
            source .venv/bin/activate
          '';
        };
      });
}
