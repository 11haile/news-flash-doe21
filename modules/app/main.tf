locals {
  region    = "eu-west1"
}


module "kubernetes-cluster" {
  source    = "../kubernetes-cluster"
  name      = var.name
  region    = var.region
}