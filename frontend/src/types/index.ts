export interface User {
    id: number
    username: string
    email: string
    wake_time: string | null
    sleep_time: string | null
    goals: string | null
    created_at: string
}

export interface Habit {
    id: number
    user: number
    name: string
    scheduled_time: string | null
    is_active: boolean
    created_at: string
}

export interface HabitLog{
    id: number
    habit: number
    date: string
    completed: boolean
    notes: string | null
}

export interface ScheduleTask{
    id: number
    schedule: number
    title: string
    time: string | null
    is_done: boolean
    category: string | null
}

export interface DaySchedule {
    id: number
    user: number
    date: string
    ai_plan: string | null
    is_completed: boolean
    created_at: string
    tasks: ScheduleTask[]
}

