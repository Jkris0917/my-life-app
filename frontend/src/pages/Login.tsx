import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { login } from '../services/auth'

export default function Login() {
    const navigate = useNavigate()
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [error, setError] = useState<string | null>(null)

    const handleSubmit = async () => {
        try {
            await login(username,password)
            navigate('/dashboard')
        } catch (err) {
            setError('Invalid username or password')
        }
    }

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-50">
            <div className="bg-white p-8 rounded-xl shadow w-full max-w-md">
                <h1 className="text-2xl font-medium mb-6">Welcome back</h1>
                {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    className="w-full border rounded-lg p-3 mb-4 text-sm"
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="w-full border rounded-lg p-3 mb-6 text-sm"
                />
                <button
                    onClick={handleSubmit}
                    className="w-full bg-purple-600 text-white py-3 rounded-lg text-sm font-medium"
                >
                    Login
                </button>
            </div>
        </div>
    )
}