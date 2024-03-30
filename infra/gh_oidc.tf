resource "aws_iam_openid_connect_provider" "gh_oidc" {
  url = "https://token.actions.githubusercontent.com"

  client_id_list = [
    "sts.amazonaws.com",
  ]

  thumbprint_list = ["cf23df2207d99a74fbe169e3eba035e633b65d94"]
}

#   "Federated" : "arn:aws:iam::012345678910:oidc-provider/token.actions.githubusercontent.com"

resource "aws_iam_role" "gh_actions_role_oidc" {
  name = "gh_actions_role_oidc"
  assume_role_policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Principal" : {
          "Federated" : "${aws_iam_openid_connect_provider.gh_oidc.id}"
        },
        "Action" : "sts:AssumeRoleWithWebIdentity",
        "Condition" : {
          "StringEquals" : {
            "token.actions.githubusercontent.com:aud" : "sts.amazonaws.com"
          },
          "StringLike" : {
            "token.actions.githubusercontent.com:sub" : "repo:PedroHPAlmeida/binance-trade-bot:*"
          }
        }
      }
    ]
  })
}
