import {MyError, ConnectionError, BadRequestError, NotAuthorizedError, NotFoundError, ForbiddenError, InvalidLinkError, ServerError} from '@/core/exceptions'

const default_status_to_error_mapping: object = {
    '400': BadRequestError,
    '401': NotAuthorizedError,
    '403': ForbiddenError,
    '404': NotFoundError,
    '418': InvalidLinkError,
    '500': ServerError
}

export class ErrorHandler{
    status_to_error_mapping: object

    constructor(status_to_error_mapping: object|undefined=undefined){
        if(status_to_error_mapping == undefined){
            status_to_error_mapping = default_status_to_error_mapping
        }
        this.status_to_error_mapping = status_to_error_mapping
    }

    get_erro_by_status(status_code: string): any{
        let error_type = this.status_to_error_mapping[String(status_code)]
        if(error_type == undefined){
            error_type = MyError
        }
        return error_type
    }

    handle(error: any): MyError {
        let new_error
        if(error.response.status){
            const error_type = this.get_erro_by_status(error.response.status)
            new_error = new error_type(error.response.data, error)
        }
        else{
            new_error = new ConnectionError("Falha de conexão", error)
        }
        console.log('error original', error)
        console.log('my error', new_error)
        return new_error
    }
}
