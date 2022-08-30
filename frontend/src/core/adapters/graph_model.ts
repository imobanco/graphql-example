import { BakcendHttpAdaptor } from "@/core/adapters/http_backend"


export class GraphQuery{
    constructor(
        public readonly query: string, 
        public readonly fields: string[], 
        public readonly input: object|undefined=undefined, 
        public readonly name: string|undefined=undefined
    ){}

    _construct_query_name(): string {
        if(this.name){
            return `${this.name}:${this.query}`
        }
        return `${this.query}`
    }

    _construct_input(): string {
        if(this.input){
            return `(input:{${
                Object.entries(this.input).map(([key, value]) => {
                    return `${key}:"${value}"`
                }).join()
            }})`
        }
        return ''
    }

    _construct_fields(): string{
        return `{${this.fields.join()}}`
    }

    construct(): string{
        return this._construct_query_name() + this._construct_input() + this._construct_fields()
    }
}


export class GraphRequest{
    constructor(
        public readonly queries: GraphQuery[]
    ){}

    constuct(){
        return {
            query: `{${this.queries.map((query) => {return query.construct()}).join('')}}`,
            variables: undefined
        }
    }
}


export class GrapModelAdapter{
    constructor(
        public readonly list_query_name: string,
        public readonly retrieve_query_name: string,
        public readonly write_query_name: string,
        public readonly default_fields: string[],
        public readonly graph_url: string='graph',
    ){}

    _get_fields(fields: string[]|undefined): string[]{
        if(fields == undefined){
            return this.default_fields
        }
        return fields
    }

    _create_request(
        query: string,
        entity_data: any=undefined, 
        fields: string[]|undefined=undefined, 
        name: string|undefined=undefined
    ): GraphRequest {
        fields = this._get_fields(fields)
        return new GraphRequest(
            [
                new GraphQuery(
                    query, fields, entity_data, name
                )
            ]
        )
    }

    async create(entity_data: any, fields: string[]|undefined=undefined, name: string|undefined=undefined): Promise<any>{
        const req = this._create_request(this.write_query_name, entity_data, fields, name)
        return await BakcendHttpAdaptor.post(this.graph_url, req.constuct())
    }

    async list(fields: string[]|undefined=undefined, name: string|undefined=undefined): Promise<any>{
        const req = this._create_request(this.list_query_name, undefined, fields, name)
        return await BakcendHttpAdaptor.post(this.graph_url, req.constuct())
    }
}