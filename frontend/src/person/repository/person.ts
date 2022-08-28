import {Person} from '@/person/entities'
import { RestModelAdapter } from '@/core/adapters/rest_model'

export class PersonRepository{

    rest_model: RestModelAdapter

    constructor(restModelAdapter: RestModelAdapter|undefined=undefined){
        if(restModelAdapter == undefined){
            restModelAdapter = new RestModelAdapter('rest/persons')
        }
        this.rest_model = restModelAdapter
    }


    async create(name: string): Promise<Person>{
        const resp = await this.rest_model.create({'name': name})
        return Person.from_data(resp.data)
    }

    async update_entity(person: Person): Promise<Person>{
        const resp = await this.rest_model.update(person.id, {'name': person.name})
        return Person.from_data(resp.data)
    }

    async update_data(person_id: string, person_data: object): Promise<Person>{
        const resp = await this.rest_model.update(person_id, person_data)
        return Person.from_data(resp.data)
    }

    // partial_update()

    // list(): Person[]

    // retrieve(id: string): Person

    // update()



    // delete()

}
