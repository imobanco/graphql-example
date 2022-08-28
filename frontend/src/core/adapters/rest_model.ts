import { BakcendHttpAdaptor } from "@/core/adapters/http_backend";
import { UrlUtils } from '@/core/utils/url'

export class RestModelAdapter{

    public model_url: string

    constructor(model_url: string){
        this.model_url = UrlUtils.remove_beggining_slash(UrlUtils.append_end_slash(model_url))
    }

    async create(entity_data: any){
        return await BakcendHttpAdaptor.post(this.model_url, entity_data)
    }

    async update(entity_id: string, entity_data: any, partial_update=true){
        const detail_url = UrlUtils.construct_url(this.model_url, entity_id)

        if(partial_update){
            return await BakcendHttpAdaptor.patch(detail_url, entity_data)
        }
        else{
            return await BakcendHttpAdaptor.put(detail_url, entity_data)
        }
    }

    async delete(entity_id: string){
        const detail_url = UrlUtils.construct_url(this.model_url, entity_id)
        return await BakcendHttpAdaptor.delete(detail_url)
    }

    async retrieve(entity_id: string){
        const detail_url = UrlUtils.construct_url(this.model_url, entity_id)
        return await BakcendHttpAdaptor.get(detail_url)
    }

    async list(query:object|undefined=undefined){
        return await BakcendHttpAdaptor.get(this.model_url, query)
    }

}
