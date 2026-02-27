use shared::{print_h2, print_h3};

pub struct BankAccount {
    owner: String,
    balance: f64,
}

impl BankAccount {
    pub fn new(owner: &str, initial: f64) -> Self {
        return BankAccount {
            owner: owner.to_string(),
            balance: initial,
        };
    }

    pub fn deposit(&mut self, amount: f64) -> Result<f64, String> {
        if amount <= 0.0 {
            return Err(format!("deposit amount must be positive, got {}", amount));
        }
        self.balance += amount;
        return Ok(self.balance);
    }

    pub fn withdraw(&mut self, amount: f64) -> Result<f64, String> {
        if amount <= 0.0 {
            return Err(format!("withdrawal amount must be positive"));
        }
        if amount > self.balance {
            return Err(format!(
                "insufficient funds: balance={}, requested={}",
                self.balance, amount
            ));
        }
        self.balance -= amount;
        return Ok(self.balance);
    }

    pub fn balance(&self) -> f64 {
        return self.balance;
    }

    pub fn owner(&self) -> &str {
        return &self.owner;
    }
}

pub fn run() {
    print_h2!("Organizing Tests");

    print_h3!("Test Module Organization");
    println!("Tests are organized in:");
    println!("  src/lib.rs or src/module.rs - unit tests in #[cfg(test)] mod tests");
    println!("  tests/                       - integration tests (separate binary)");
    println!("  benches/                     - benchmarks (criterion crate)");
    println!("  examples/                    - runnable examples");

    print_h3!("Running Tests");
    println!("cargo test                       - run all tests");
    println!("cargo test -p testing            - run tests in this package");
    println!("cargo test test_deposit          - run tests matching 'test_deposit'");
    println!("cargo test -- --nocapture        - show println! output");
    println!("cargo test -- --test-threads=1  - run tests serially");
    println!("cargo test -- --include-ignored  - also run #[ignore] tests");

    print_h3!("BankAccount demo");
    let mut acc: BankAccount = BankAccount::new("Alice", 1000.0);
    println!("Owner: {}", acc.owner());
    println!("Balance: {}", acc.balance());
    println!("deposit(500) = {:?}", acc.deposit(500.0));
    println!("withdraw(200) = {:?}", acc.withdraw(200.0));
    println!("withdraw(9999) = {:?}", acc.withdraw(9999.0));
}

#[cfg(test)]
mod tests {
    use super::*;

    // No built-in before_each, but helper fns work fine

    fn make_account() -> BankAccount {
        return BankAccount::new("Test User", 500.0);
    }

    #[test]
    fn test_new_account_balance() {
        let acc: BankAccount = make_account();
        assert_eq!(acc.balance(), 500.0);
        assert_eq!(acc.owner(), "Test User");
    }

    #[test]
    fn test_deposit_increases_balance() {
        let mut acc: BankAccount = make_account();
        let result: Result<f64, String> = acc.deposit(100.0);
        assert_eq!(result, Ok(600.0));
        assert_eq!(acc.balance(), 600.0);
    }

    #[test]
    fn test_withdraw_decreases_balance() {
        let mut acc: BankAccount = make_account();
        let result: Result<f64, String> = acc.withdraw(200.0);
        assert_eq!(result, Ok(300.0));
        assert_eq!(acc.balance(), 300.0);
    }

    #[test]
    fn test_multiple_operations() {
        let mut acc: BankAccount = make_account();
        acc.deposit(1000.0).unwrap();
        acc.withdraw(250.0).unwrap();
        acc.deposit(50.0).unwrap();
        assert_eq!(acc.balance(), 1300.0);
    }

    #[test]
    fn test_deposit_negative_returns_error() {
        let mut acc: BankAccount = make_account();
        let result: Result<f64, String> = acc.deposit(-50.0);
        assert!(result.is_err());
        assert!(result.unwrap_err().contains("positive"));
    }

    #[test]
    fn test_deposit_zero_returns_error() {
        let mut acc: BankAccount = make_account();
        assert!(acc.deposit(0.0).is_err());
    }

    #[test]
    fn test_withdraw_insufficient_funds() {
        let mut acc: BankAccount = make_account();
        let result: Result<f64, String> = acc.withdraw(9999.0);
        assert!(result.is_err());
        let err: String = result.unwrap_err();
        assert!(err.contains("insufficient funds"), "got: {}", err);
    }

    #[test]
    fn test_withdraw_exact_balance() {
        let mut acc: BankAccount = make_account();
        let result: Result<f64, String> = acc.withdraw(500.0); // exactly the balance
        assert_eq!(result, Ok(0.0));
    }

    // Grouping by feature/behavior is common

    // Nested test modules are valid Rust modules — they inherit #[cfg(test)] from the parent
    mod deposit_tests {
        use super::*;

        #[test]
        fn test_large_deposit() {
            let mut acc: BankAccount = make_account();
            acc.deposit(1_000_000.0).unwrap();
            assert_eq!(acc.balance(), 1_000_500.0);
        }

        #[test]
        fn test_fractional_deposit() {
            let mut acc: BankAccount = make_account();
            acc.deposit(0.01).unwrap();
            assert!((acc.balance() - 500.01).abs() < 1e-9);
        }
    }

    mod withdraw_tests {
        use super::*;

        #[test]
        fn test_withdraw_to_zero() {
            let mut acc: BankAccount = make_account();
            acc.withdraw(500.0).unwrap();
            assert_eq!(acc.balance(), 0.0);
        }

        #[test]
        fn test_withdraw_zero_amount() {
            let mut acc: BankAccount = make_account();
            assert!(acc.withdraw(0.0).is_err());
        }
    }
}
