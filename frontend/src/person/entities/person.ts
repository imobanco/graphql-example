import {BaseModelc} from '@/core/entities'

export class Person extends BaseModelc{
    constructor(
        public name: string,
        id: string,
        created_at: Date,
        updated_at: Date,
    ){
        super(id, created_at, updated_at)
    }

    to_object(){
        return {
            'id': this.id,
            'created_at': this.created_at,
            'updated_at': this.updated_at,
            'name': this.name,
        }
    }

    update_from_data(person_data: any){
        this.name = person_data.name
        this.id = person_data.id
        this.created_at = person_data.created_at
        this.updated_at = person_data.updated_at
    }

    static from_data(person_data: any){
        return new Person(
            person_data.name, 
            person_data.id, 
            person_data.created_at, 
            person_data.updated_at
        )
    }
}
