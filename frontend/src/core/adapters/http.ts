import axios from 'axios'
import { ErrorHandler } from '@/core/exceptions'
import { UrlUtils } from '@/core/utils/url'


export class HttpAdaptor{
    public readonly base_url: string
    public readonly custom_error_handler: ErrorHandler

    constructor(base_url: string, custom_handler:ErrorHandler|undefined=undefined){
        this.base_url = UrlUtils.append_end_slash(base_url)
        if(custom_handler == undefined){
            custom_handler = new ErrorHandler()
        }
        this.custom_error_handler = custom_handler
    }

    handle_error(error: any, raise:Boolean=true){
        let new_error = this.custom_error_handler.handle(error)
        if(raise){
            throw new_error
        }
        return new_error
    }

    async handle_promise(promise: Promise<any>){
        try{
            return await promise
        }
        catch(error){
            this.handle_error(error)
        }
    }

    async get(url: string, query: object|undefined=undefined){
        const new_url = UrlUtils.construct_url(this.base_url, url) + UrlUtils.construct_query(query)
        const promise = axios.get(new_url)
        return await this.handle_promise(promise)
    }

    async post(url: string, data: any, query: object|undefined=undefined){
        const new_url = UrlUtils.construct_url(this.base_url, url) + UrlUtils.construct_query(query)
        const promise = axios.post(new_url, data)
        return await this.handle_promise(promise)
    }

    async put(url: string, data: object, query: object|undefined=undefined){
        const new_url = UrlUtils.construct_url(this.base_url, url) + UrlUtils.construct_query(query)
        const promise = axios.put(new_url, data)
        return await this.handle_promise(promise)
    }

    async patch(url: string, data: object, query: object|undefined=undefined){
        const new_url = UrlUtils.construct_url(this.base_url, url) + UrlUtils.construct_query(query)
        const promise = axios.patch(new_url, data)
        return await this.handle_promise(promise)
    }

    async delete(url: string, data: object|undefined=undefined, query: object|undefined=undefined){
        const new_url = UrlUtils.construct_url(this.base_url, url) + UrlUtils.construct_query(query)
        const promise = axios.delete(new_url, {'data': data})
        return await this.handle_promise(promise)
    }
}

