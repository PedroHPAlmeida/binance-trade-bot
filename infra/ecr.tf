resource "aws_ecr_repository" "ecr_repository_binance_trades" {
  name = "binance-trades-bot"
  force_delete = true
}
