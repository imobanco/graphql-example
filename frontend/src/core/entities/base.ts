export class BaseModelc{
    constructor(
        public id: string,
        public created_at: Date,
        public updated_at: Date,
    ){}
}



export type BaseModel = {
    id: string
    created_at: string
    updated_at: string
}