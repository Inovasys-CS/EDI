# EDI: Emulation, Detection, and Intelligence - Detection Use Cases Repository

Pronounced "Eddy", this repository aims to collect and structure all the detection use cases based on the MITRE ATT&CK framework. Our goal is to provide a comprehensive resource for security professionals to develop effective detection strategies against cyber threats.

## Structure

The repository is structured according to the MITRE ATT&CK framework, organizing detection use cases by tactics and techniques. Each technique includes detailed information about detection strategies, including:

- **Sigma File**: Sigma rules for implementing detection logic in SIEM solutions.
- **Atomic Tests**: Atomic Red Team tests to validate the effectiveness of detection rules.
- **Logs (if available)**:  Sample logs or data to demonstrate the behavior associated with the technique.

## Bundles

In addition to individual detection use cases, we provide bundles that collect the latest reports for threat detection & intelligence. These bundles consolidate all covered detection use cases, making it easier for users to download and implement them in their security operations.

It's easy to export all the rules associated with a bundle by using the bundle exporter script found in the [utils directory](https://github.com/Inovasys-CS/EDI/tree/main/utils). You can also find more information about the bundle format in the [utils README](https://github.com/Inovasys-CS/EDI/blob/main/utils/README.md)

## CVEs Coverage

We also cover the latest Common Vulnerabilities and Exposures (CVEs) to make it easier for you to fortify yourself against known vulnerabilities. By integrating CVE data into our detection use cases, we aim to provide a holistic approach to threat detection and mitigation.

## Contributors

This repository is supported by Inovasys and written by its Blue Team members. Inovasys is committed to advancing cybersecurity knowledge and sharing best practices within the community.

## Contributing

We encourage contributions from the cybersecurity community to enhance the repository's comprehensiveness and accuracy. If you have new detection use cases, improvements to existing ones, or additional threat intelligence reports to share, please feel free to submit pull requests or open issues.

## License

This repository is licensed under the [MIT License](LICENSE), which means you are free to use, modify, and distribute the content for both commercial and non-commercial purposes. However, attribution to the original source is appreciated.

---

*Disclaimer: This repository is provided for educational and informational purposes only. Use at your own risk.*