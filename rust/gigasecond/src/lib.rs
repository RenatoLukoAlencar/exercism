use time::Duration;
use time::PrimitiveDateTime as DateTime;

// Returns a DateTime one billion seconds after start.
pub fn after(start: DateTime) -> DateTime {
    let giga_seconds = 1000000000;

    return start + Duration::seconds(giga_seconds);
}
