terraform {
  cloud {
    organization = "binance-trades-bot"

    workspaces {
      name = "binance-trades"
    }
  }
}
