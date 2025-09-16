def serve_chai(flavour):
    try:
        print(f"Preparing {flavour} chai...")
        if flavour == "unknown":
            raise ValueError("Unknown flavour")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavour} chai is served")
    finally:
        print("Cleaning up resources")

serve_chai("unknown")
serve_chai("masala")