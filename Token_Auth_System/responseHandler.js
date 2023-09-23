const badRequest = (res, data) => {
	return res.status(400).json({
		error: "Bad Request",
		status: 400,
		message: data
	})
}

const serverError = (res, data) => {
	return res.status(500).json({
		error: "Internal Server Error",
		status: 500,
		message: data
	})
}

const success = (res, data) => {
	return res.status(200).json({
		message: "Success",
		status: 200,
		data
	})
}

const unauthorize = (res, data) => {
	return res.status(401).json({
		error: "Unauthorized",
		status: 401,
		message: data
	})
}

module.exports = { badRequest, serverError, success, unauthorize }
