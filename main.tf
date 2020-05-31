terraform {
 backend "remote" {
   organization = "sebasibarguen"

   workspaces {
     name = "convo"
   }
 }
}

resource "null_resource" "terraform-github-actions" {
 triggers = {
   value = "This resource was created using GitHub Actions!"
 }
}

provider "heroku" {
  version = "~> 2.4"
}

variable "app_name" {
  description = "Convo API"
}

resource "heroku_app" "app" {
  name   = var.app_name
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
  size       = "Standard-1x"
  depends_on = [heroku_build.app]
}

output "app_url" {
  value = "https://${heroku_app.app.name}.herokuapp.com"
}