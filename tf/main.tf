provider "aws" {
  version = "~> 2.64"
  region  = "us-east-1"
}

terraform {
 backend "s3" {
   bucket = "convo-deploy"
   key = "tf/terraform.tfstate"
   region = "us-east-1"
 }
}

resource "aws_s3_bucket" "terraform_state" {
  bucket = "convo-deploy"

  versioning {
    enabled = true
  }
}