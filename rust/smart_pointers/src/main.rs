#![allow(dead_code)]
use shared::print_h1;

mod arc_pointer;
mod box_pointer;
mod cow;
mod mutex_rwlock;
mod once_lock;
mod patterns;
mod rc_pointer;
mod refcell;

fn main() {
    print_h1!("Smart Pointers");

    box_pointer::run();

    rc_pointer::run();

    arc_pointer::run();

    refcell::run();

    mutex_rwlock::run();

    patterns::run();

    cow::run();

    once_lock::run();
}
