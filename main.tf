provider "google" {
  project = "kalyan-devops-2025"
  region  = "us-central1"
}

resource "google_compute_network" "vpc" {
  name                    = "my-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet" {
  name          = "my-subnet"
  ip_cidr_range = "10.0.0.0/16"
  region        = "us-central1"
  network       = google_compute_network.vpc.id
}

resource "google_container_cluster" "gke_cluster" {
  name     = "my-gke-cluster"
  location = "us-central1"
  network  = google_compute_network.vpc.name
  subnetwork = google_compute_subnetwork.subnet.name

  remove_default_node_pool = true
  initial_node_count       = 1
}

resource "google_container_node_pool" "node_pool" {
  name       = "my-node-pool"
  location   = "us-central1"
  cluster    = google_container_cluster.gke_cluster.name
  node_count = 3

  node_config {
    machine_type = "e2-medium"
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}