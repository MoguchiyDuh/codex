---
tags:
  - computing/signals
  - analog
  - digital
  - adc
related:
  - "[[Data Representation]]"
  - "[[Number Systems]]"
  - "[[00 - Computing MOC]]"
---

1. **Analog** (continuous) -  signal that varies continuously over time
	- It can take on any value within a range, not just discrete levels
	- Example:
		- The voltage from a microphone when someone is speaking.
		- A sine wave representing an alternating current (AC).
		- Sound waves in air (e.g., someone speaking)
		- Temperature measured by a traditional mercury thermometer
	
![[analog_signal.excalidraw]]
Key properties of analog signals:
- *Amplitude*: How “tall” the wave is (e.g., voltage level).
- *Frequency*: How fast the wave oscillates.
- *Phase*: The position of the wave relative to a reference.

2. **Digital**  -  signal that varies in discrete steps (not continuous, has less errors then analog because represented by two numbers so it is hard to misrepresent the response) 
	- Levels of voltage: 
		- *low voltage* (0V) -> $0_{(2)}$
		- *high voltage* (3.3V, 5V) -> $1_{(2)}$
	- Key properties of digital signals:
		- Discrete levels (usually binary: 0 or 1).
		- Time is sampled at intervals (discrete time behavior in circuits).
		- Each step is clearly distinguishable — no “in-between” states are valid.
	*Resolution* - the set of values system can represent
	
## Why Digital  for computers?
2.  **Noise immunity**
	- Real-world signals are never perfect — *they pick up noise* (random unwanted variations).
	- If a computer used analog signals directly, *even tiny amounts of noise would change computations*.
	- Digital signals are *robust*:
		- As long as the noise does not cross the threshold *between 0 and 1*, the signal is still interpreted correctly.
3. **Precision** and **repeatability** 
	- Analog systems degrade in accuracy over time due to *component tolerances*.
	- *Digital representation* allows exact storage and precise replication (e.g., copying file perfectly).
4. **Ease of design with logic**
	- *Boolean algebra* works naturally with binary signals.
	- This allows simple, scalable *logic circuits*.
5. **Scalability** and **integration**
	- *Billions* of transistors on modern CPUs are practical because digital transistors only need to distinguish two states (on/off).
	- Analog circuits for the same complexity would be *fragile* and *impractical*

## Noise and its Effect
1. **Noise** is any unwanted variation added to a signal. It comes from:
	- *Thermal fluctuations* in resistors and transistors
	- *Electromagnetic interference* (from other circuits, radio waves, etc.)
	- *Imperfect transmission lines*
2.  Analog case:
	- If you transmit an analog signal (e.g., voltage proportional to sound), *noise directly changes the value*.
	- Over long distances or repeated processing, the original signal becomes *distorted and degraded*.
	- Example: Old analog cassette tapes or VHS — each copy reduces quality.
3. Digital case:
	- A digital signal only needs to be *above* or *below* a threshold.
	- Small noise changes the wave shape but not the interpretation of 0 or 1.
	- Example: A scratched CD still plays correctly because the digital encoding can tolerate noise (and often use error correction).

## Why Analog Copies Deteriorate but Digital Does Not
 1. Analog Copying
	- Each time you copy an analog signal (e.g., cassette tape → another tape), *noise and distortion accumulate*:
	- Tape *hiss*, *static*, *frequency loss*, and *slight shifts in amplitude*.
	- The copied signal is never identical to the original.
	- Repeated copying *degrades* quality further — the error compounds.
2. Digital Copying
	- A digital signal is stored as binary (0s and 1s).
	- When copied, the computer checks whether each bit is above or below a threshold.
	- As long as the noise doesn’t flip a bit across the threshold, the copy is exactly identical to the original.
	- Even if noise is present, error-correcting codes (ECC, parity, etc.) can restore correctness.
	- You can copy a digital file a million times, and it remains bit-for-bit identical.
## ADC:
![[adc.excalidraw]]
1. Sampling
	- Take *discrete measurements* of the signal at fixed intervals.
	- The rate is called the *sampling frequency* (measured in Hz).
	- Example: CD audio uses 44.1 kHz → 44,100 samples per second.
2. Quantisation
	- Each sample’s amplitude is mapped to the *nearest discrete level*.
	- The number of levels depends on *bit depth*.
		- 8-bit → 256 possible levels
		- 16-bit → 65,536 levels
		- Higher bit depth → better precision. 
	- n bits => $2^n$ possible levels
3. Encoding
	- Each quantized value is stored as a binary number.
	- This sequence of binary values is the digital representation of the original analog signal.


---

## See Also
- [[Data Representation]] - Binary representation of data
- [[Number Systems]] - Number conversions
- [[00 - Computing MOC]] - Computing topics overview
