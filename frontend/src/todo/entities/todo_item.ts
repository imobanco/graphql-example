import type {BaseModel} from '@/core/entities'
import type {Todo} from './todo'


export type TodoItem = BaseModel & {
    name: String
    done: boolean
    todo: Todo
}