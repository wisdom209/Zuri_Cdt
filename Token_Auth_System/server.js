const express = require('express')
const dotenv = require('dotenv')
const jwt = require('jsonwebtoken')

const responseHandler = require('./responseHandler')

dotenv.config()
const app = express()
const port = process.env.PORT || 4000
const JWT_SECRET = process.env.JWT_SECRET || 'sfashgfhasfgosehfsafhb'

app.use(express.json())

const test_username = process.env.USERNAME || "Gold123"
const test_password = process.env.PASSWORD || "password123"


app.post('/login', (req, res) => {
	try {
		const { username, password } = req.body

		if (!username || !password) return responseHandler.badRequest(res, "Missing field details")

		if (username != test_username || password != test_password) {
			return responseHandler.badRequest(res, "Invalid credentials")
		}

		const token = jwt.sign({ username, password }, JWT_SECRET, { expiresIn: '2d' })

		return responseHandler.success(res, { token, username, password })

	} catch (error) {
		return responseHandler.serverError(res, error.message)
	}
})


app.get('/', (req, res) => {
	try {
		const auth_header = req.headers?.authorization

		if (!auth_header) return responseHandler.unauthorize(res, "No authorization header")

		const token = auth_header.split(' ')[1]

		if (!token) return responseHandler.unauthorize(res, "Invalid or no authorization token")

		const userDetail = jwt.verify(token, JWT_SECRET)

		if (userDetail?.username != test_username || userDetail?.password != test_password) {
			return responseHandler.unauthorize("Invalid or no authorization token")
		}

		return responseHandler.success(res, {
			username: userDetail.username,
			password: userDetail.password
		})
	} catch (error) {
		return responseHandler.serverError(res, error.message)
	}
})

app.listen(port, () => {
	console.log("Server is listening on port", port)
})
