export class BaseModelc{
    constructor(
        public readonly id: string,
        public readonly created_at: Date,
        public readonly updated_at: Date,
    ){}
}



export type BaseModel = {
    id: string
    created_at: string
    updated_at: string
}