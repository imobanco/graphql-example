{
  description = "Este é o nix (com flakes) para o ambiente de desenvolvimento do frontend";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils
  }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        name = "backend";

        pkgsAllowUnfree = import nixpkgs {
          inherit system;
          config = { allowUnfree = true; };
        };

        pkgsAllowUnfreeAllowBroken = import nixpkgs {
          inherit system;
          config = {
            allowUnfree = true;
            allowBroken = true;
          };
        };

        minimal-required-packages = with pkgsAllowUnfree; [
          bash
          coreutils
          gnumake
        ];

      in
      rec {
        packages.default = packages.${name};
        devShell = pkgsAllowUnfree.mkShell {
          buildInputs = with pkgsAllowUnfree; [
            curl
            gnumake
            nodejs
            yarn
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

