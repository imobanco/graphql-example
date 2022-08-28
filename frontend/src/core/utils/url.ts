export class UrlUtils{
    static append_end_slash(url: string){
        if(url.slice(-1) != '/'){
            return url + '/'
        }
        return url
    }

    static remove_beggining_slash(url: string){
        if(url.slice(0, 1) == '/'){
            return url.slice(1)
        }
        return url
    }

    static construct_query(query: object|undefined){
        let query_url = '?'
        if(query == undefined){
            return query_url
        }
        try{
            Object.entries(query).forEach(([key, value])=> {
                query_url += `${key}=${value}&`
            })
        }
        finally{
            return query_url
        }
    }

    static construct_url(base_url: string, other_url: string){
        const url = UrlUtils.append_end_slash(base_url)+ UrlUtils.remove_beggining_slash(other_url)
        return UrlUtils.append_end_slash(url)
    }
}