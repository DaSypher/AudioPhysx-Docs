# Interfaces and external audio parameters

AudioPhysx separates gameplay-side world queries from audio rendering. One consequence is that some MetaSound inputs are fed by named parameters or registered interfaces rather than being authored independently in each graph. These names and data types are **contracts**. They should not be approximated by creating visually similar inputs with arbitrary spelling.

## The compact selected acoustic route

The current source includes a selected-route Float Array named `AP.AcousticRoute.Selected`. It is intended for the [Acoustic Paths](nodes/acoustics/acoustic-paths.md) processor, and the values must follow the same order as the source-side contract:

```text
[delay ms, low loss dB, mid loss dB, high loss dB]
```

The world path solver decides whether direct or around-obstacle sound should be selected; the MetaSound processor applies the corresponding delay and three-band loss. Keeping the route together in one array reduces the possibility that the delay comes from a different query update than the spectral losses. The convenience does make the ordering more important, so verify the exact array before trying to correct an unexpected filter result.

Other AudioPhysx systems expose atmosphere, transmission, impact and propagation values through their current interfaces. Where an installed build supplies those interfaces, use the actual registered names and types. Do not construct an independent parameter solely from an old screenshot if the current interface has changed. MetaSound asset interface migrations and configurable surface-route changes can affect how saved graphs reconnect.

The flyby subsystem has a separate set of five named Float inputs beginning with `AP.Flyby.`. Those are documented on the [Flyby Blueprint page](../blueprint/flyby.md). All such interfaces carry **control values or triggers**: they do not change the fact that the audio processors themselves now carry stereo Left and Right buffers.
