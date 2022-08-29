import {Person} from '@/person/entities'
import { RestModelAdapter } from '@/core/adapters/rest_model'

export class PersonRepository{

    rest_model: RestModelAdapter

    constructor(restModelAdapter: RestModelAdapter|undefined=undefined){
        if(restModelAdapter == undefined){
            restModelAdapter = new RestModelAdapter('/rest/persons/')
        }
        this.rest_model = restModelAdapter
    }

    get_empty_entity(): Person{
        return new Person(undefined, undefined, undefined, undefined)
    }

    async create(person: Person): Promise<Person>{
        const resp = await this.rest_model.create({'name': person.name})
        person.update_from_data(resp.data)
        return person
    }

    async update(person: Person): Promise<Person>{
        const resp = await this.rest_model.update(person.id, {'name': person.name})
        person.update_from_data(resp.data)
        return person
    }


    // partial_update()

    // list(): Person[]

    // retrieve(id: string): Person

    // update()


    // delete()

}
