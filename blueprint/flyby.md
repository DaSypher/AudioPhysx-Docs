# Flyby integration in Blueprint

The AudioPhysx flyby helpers are designed to accept projectile-path information without requiring Chaos physics simulation.

## General integration

1. Prepare a MetaSound Source using `AP: Flyby Wave Player` with suitable whizz and crack arrays.
2. From your weapon/projectile logic, supply the path start, path end, projectile speed and optional projectile identity to the AudioPhysx flyby helper.
3. A qualifying near miss can be scheduled at the calculated closest-pass position and estimated arrival time.
4. Test shots that miss by a small distance, shots outside the audible range and shots that pass behind obstacles.

The first version uses simplified constant-speed near-miss and acoustic timing. It should not be presented as a fully physically accurate ballistic model.

> TODO: Add a screenshot of the actual Blueprint function signature; verify parameter names, timing model, and world-subsystem behaviour against the Shipping build.
