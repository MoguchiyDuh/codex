use shared::print_h1;

mod async_basics;
mod channels;
mod patterns;
mod rayon_parallel;
mod shared_state;
mod threads;
mod tokio_channels;
mod tokio_runtime;

#[tokio::main]
async fn main() {
    print_h1!("Concurrency and Parallelism");

    threads::run();
    channels::run();
    shared_state::run();
    async_basics::run().await;
    tokio_runtime::run().await;
    tokio_channels::run().await;
    rayon_parallel::run();
    patterns::run().await;
}
