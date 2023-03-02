locals {
  region    = "fra1"
}


module "kubernetes-cluster" {
  source    = "../kubernetes-cluster"
  name      = var.name
  region    = var.region
  version   = var.version
  size      = var.size
}