export class MyError{
    public original_error: any
    public data: any
    public type: string

    constructor(data: any, original_error: any=undefined){
        this.original_error = original_error
        this.data = data
        this.type = this.constructor.name
    }
}


export class ConnectionError extends MyError{}

export class NotFoundError extends MyError{}

export class BadRequestError extends MyError{}

export class InvalidLinkError extends MyError{}

export class NotAuthorizedError extends MyError{}

export class ForbiddenError extends MyError{}

export class ServerError extends MyError{}