data "digitalocean_kubernetes_cluster" "example" {
  name = "prod-cluster-01"
}

provider "kubernetes" {
  host             = data.digitalocean_kubernetes_cluster.example.variable.endpoint
  token            = data.digitalocean_kubernetes_cluster.example.kube_config[0].token
  cluster_ca_certificate = base64decode(
    data.digitalocean_kubernetes_cluster.example.kube_config[0].cluster_ca_certificate
  )
}