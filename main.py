@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json() or request.form
    input_data = data.get("input")

    if not input_data:
        return jsonify({
            "status": "error",
            "message": "No input provided"
        })

    # ---------------------------
    # SAFE INPUT HANDLING
    # ---------------------------
    try:
        input_data_numeric = float(input_data)
    except:
        input_data_numeric = input_data  # keep string if not numeric

    # SAST validation
    if not validate_input(input_data_numeric):
        return jsonify({
            "status": "blocked",
            "result": "Malicious Input Detected (SAST Layer)"
        })

    # DAST / ML detection
    result = detect_attack(input_data_numeric)

    return jsonify({
        "mode": "Live Detection",
        "input": input_data,
        "result": str(result)
    })