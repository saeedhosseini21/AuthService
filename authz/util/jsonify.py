from flask import current_app

DEBUG_MSG_CODES = {
  "100": "ok",
  "101": "unsupported Media Type",
  "102": "Database Error",
  "103": "Resource Not Found",
  "104": "Request Validation Failed",
  "105": "Empty Data Supplied",
  "106": "Resource Conflict",
  "107": "Not Implemented."
}

def jsonify(state={}, metadata={}, status=200, code=100, headers={}):
	data = state
	data.update(metadata)
	if current_app.debug:
		data["message"] = DEBUG_MSG_CODES[str(code)]
	data["code"] = code
	return data, status, headers
	
	
