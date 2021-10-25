from Spectra import Assistant


if __name__ == "__main__":
    Serve = Assistant.Assistant(debug = True, autoupdate=True)
    Serve.Start()