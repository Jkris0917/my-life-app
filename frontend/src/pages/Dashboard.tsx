import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { logout, isAuthenticated } from '../services/auth'
import api from '../services/api'
import type { DaySchedule } from '../types'

export default function Dashboard() {
    const navigate = useNavigate()
    const [schedule, setSchedule] = useState<DaySchedule | null>(null)
    const [loading, setLoading] = useState(false)

    useEffect(() => {
        if (!isAuthenticated()) {
            navigate('/')
        }
    }, [navigate])

    const handleGenerateSchedule = async () => {
        setLoading(true)
        try {
            const response = await api.post('/generate-schedule/')
            setSchedule(response.data)
        } catch (err) {
            console.error(err)
        } finally {
            setLoading(false)
        }
    }

    const handleLogout = () => {
        logout()
        navigate('/')
    }

    return (
        <div className="min-h-screen bg-gray-50 p-6">
            <div className="max-w-2xl mx-auto">
                <div className="flex justify-between items-center mb-6">
                    <h1 className="text-2xl font-medium">My Day</h1>
                    <button
                        onClick={handleLogout}
                        className="text-sm text-gray-500 hover:text-gray-700"
                    >
                        Logout
                    </button>
                </div>

                <button
                    onClick={handleGenerateSchedule}
                    disabled={loading}
                    className="w-full bg-purple-600 text-white py-3 rounded-xl text-sm font-medium mb-6"
                >
                    {loading ? 'Generating...' : 'Generate My Day'}
                </button>

                {schedule && (
                    <div className="bg-white rounded-xl p-6 shadow-sm">
                        <p className="text-sm text-gray-500 mb-4">{schedule.date}</p>
                        <p className="text-lg font-medium">{schedule.ai_plan}</p>
                    </div>
                )}
            </div>
        </div>
    )
}