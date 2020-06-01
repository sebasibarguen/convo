provider "heroku" {
  version = "~> 2.4"
}

locals {
  app_name = "convo-apix"
}

resource "heroku_app" "app" {
  name   = local.app_name
  region = "us"

  stack = "container"
}

# Build code & release to the app
resource "heroku_build" "app" {
  app = heroku_app.app.id

  source = {
    path = "."
  }
}

# Launch the app's web process by scaling-up
resource "heroku_formation" "app" {
  app        = heroku_app.app.name
  type       = "web"
  quantity   = 1
  size       = "free"
  depends_on = [heroku_build.app]
}

output "app_url" {
  value = "https://${heroku_app.app.name}.herokuapp.com"
}