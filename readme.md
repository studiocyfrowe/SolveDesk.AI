# AI Service (SolveDesk.ai)

Warstwa odpowiedzialna za inteligentne przetwarzanie zgłoszeń.

Funkcjonalności:

* wyszukiwanie podobnych zgłoszeń (vector search)
* generowanie odpowiedzi (LLM)
* tworzenie embeddingów (BERT)
* kategoryzacja zgłoszeń (K-Means)
* przetwarzanie asynchroniczne

Technologie:

* Python
* BERT / embeddings
* LLM
* Scikit-learn (K-Means)
* vector database
* cosine similarity

---

## Key Features

* semantyczne wyszukiwanie zgłoszeń
* automatyczne generowanie odpowiedzi przez LLM
* klasyfikacja zgłoszeń przy użyciu ML
* centralna baza wiedzy
* architektura modularna (backend + AI + frontend)

---

## Examples

### Wyszukiwanie semantyczne

#### [POST] /api/search

**Request
```json

{
  "query": "Printing issues",
  "top_k": 6
}

```

**Response Body
```json

{
  "query": "Printing issues",
  "solutions": [
    {
      "issue_id": "cd359ffa-a4ab-4fc6-8c59-7ca60d2ee54a",
      "issue_name": "Canon PIXMA MG3620 Issue",
      "issue_sympthoms": "I'm experiencing a paper jam and error message while using wireless printing with Canon PIXMA MG3620. Can you provide guidance on resolving this?",
      "issue_solution": "Subject: Re: Canon PIXMA MG3620 Issue\n\nHi,\n\nTo resolve the paper jam, turn off the printer and gently remove jammed paper from the input/output tray area. For wireless errors, ensure the printer is connected to the Wi-Fi network. If issues persist, reset your printer and router. \n\nBest, \n<name>",
      "score": 0.77
    },
    {
      "issue_id": "cc0d7329-1f7c-4f89-a99b-be53ec7cda52",
      "issue_name": "",
      "issue_sympthoms": "Dear Customer Support Team,\n\nI am writing to seek assistance with an issue I am facing with the HP DeskJet 3755 printer that I recently purchased from Tech Online Store. Upon setting up the printer for the first time, I noticed that the printouts are consistently coming out in low quality, which is quite disappointing given the high expectations associated with this model.\n\nI have ensured that all the preliminary setup steps were followed as per the user manual. The ink cartridges are new, fitted correctly, and have not been refilled. I have also performed a nozzle check and aligned the print head, yet the print quality remains subpar. I have tried different types of paper and adjusted the printer settings according to the recommenda-tions, but unfortunately, nothing seemed to improve the situation.\n\nCould you please guide me through any advanced troubleshooting steps that might address this issue? Or is there a possibility that there could be a defective component in the printer itself? If necessary, I am open to the idea of exchanging or replacing the unit, as I rely heavily on quality printouts for my personal projects. I hope to resolve this matter swiftly.\n\nThank you for your understanding and support. I look forward to your swift response to help resolve the matter.\n\nSincerely,\n\n<name>\n<acc_num>",
      "issue_solution": "Dear <name>,\n\nThank you for reaching out to us regarding the issue with your HP DeskJet 3755 printer. I understand how important it is for you to achieve high-quality printouts.\n\nGiven the steps you've already taken, I recommend trying the following advanced troubleshooting steps:\n\n1. **Clean the Printhead:** Check if your printer software has a printhead cleaning utility. Sometimes, additional cleaning cycles can resolve issues.\n\n2. **Driver Updates:** Ensure that the printer driver is up to date by visiting the HP support website and downloading any available updates.\n\n3. **Printer Firmware:** Check for any available firmware updates on the HP website that could rectify this issue.\n\n4. **Original HP Cartridges:** Although your ink cartridges are new, ensure they are original HP cartridges, as third-party cartridges may sometimes cause quality issues.\n\n5. **Contact HP Support:** There could be specific issues related to your printer model that HP is aware of and could provide solutions for.\n\nIf after following these steps the issue persists, there might indeed be a component issue with the printer. We can assist you with the process of exchanging or replacing the unit. Please let us know your preferred course of action.\n\nWe value your satisfaction and are committed to solving this issue promptly.\n\nBest regards,\n\nCustomer Support Team",
      "score": 0.761
    },
    {
      "issue_id": "cd7c5210-d516-4ebb-a1a3-af0baa4e2874",
      "issue_name": "Requesting Assistance for Printer Paper Jam Error",
      "issue_sympthoms": "Hello Customer Support Team,\n\nI am experiencing a continuous issue with my Canon PIXMA MG3620 printer. Whenever I attempt to utilize the all-in-one wireless printing functionality, a paper jam error repeatedly occurs, making it impossible to proceed with my printing tasks. Despite several attempts to resolve this on my own, the error persists.\n\nI purchased this printer a few months ago from your Tech Online Store and have been encountering this problem ever since. Could you please provide guidance on how to troubleshoot this issue or facilitate a replacement if necessary?\n\nI appreciate your prompt assistance in this matter as it is affecting my daily work tasks. Thank you in advance.\n\nBest regards,\n\n<name>",
      "issue_solution": "Subject: Re: Requesting Assistance for Printer Paper Jam Error\n\nHello <name>,\n\nWe are sorry to hear about the repeated paper jam issue with your Canon PIXMA MG3620. Please try the following troubleshooting steps:\n\n1. Turn off your printer and disconnect it from the power source.\n2. Open the front cover and remove any jammed paper.\n3. Ensure that the paper tray is not overfilled.\n4. Realign the paper and close the printer properly.\n5. Turn the printer back on and try printing again.\n\nIf the problem persists, it might be a hardware-related fault. Given that you recently purchased this printer from our Tech Online Store, please provide your purchase details for warranty check and replacement options.\n\nWe're committed to resolving this quickly to minimize disruption to your work.\n\nBest regards,\n\nCustomer Support Team",
      "score": 0.759
    },
    {
      "issue_id": "aef59314-963b-4163-853b-ba46770c59a3",
      "issue_name": "Frequent Paper Jam Issues: HP DeskJet 3755",
      "issue_sympthoms": "Dear Customer Support,\n\nI am experiencing frequent paper jam issues with my HP DeskJet 3755 printer, especially when printing multiple pages. This has become a consistent problem and greatly disrupts my ability to efficiently print documents. I would appreciate any troubleshooting steps or advice you can provide to help resolve this issue. I look forward to your guidance or if necessary, additional support.\n\nThank you for your assistance.\n\nBest Regards,\n<name>",
      "issue_solution": "Dear <name>,\n\nI'm sorry to hear about the issues with your HP DeskJet 3755. To resolve the paper jams, please try the following: 1. Remove any jammed paper from the input and output trays. 2. Use recommended paper types and make sure no sheets are stuck together. 3. Clean the paper rollers using a lint-free cloth. 4. Ensure the printer is on a flat, stable surface. If problems persist, please contact us for further support.\n\nBest Regards,  \nCustomer Support",
      "score": 0.746
    },
    {
      "issue_id": "2e9c0355-4f4f-4cc1-a1ec-40a368d5f7f7",
      "issue_name": "Assistance Required for Persistent Paper Jam Issues with Canon Printer",
      "issue_sympthoms": "Dear Customer Support,\n\nI am writing to report persistent paper jam issues with my Canon PIXMA MG3620 printer. The problem occurs during light checkout documentation printing. I have ensured that the paper is not overloaded, and I have also checked for any visible obstructions. Despite these efforts, the issue persists. Could you please provide me with further assistance or suggest any additional troubleshooting steps? My printer's serial number is <acc_num>.\n\nThank you for your prompt attention to this matter.\n\nBest regards,\n<name>\n<tel_num>",
      "issue_solution": "Dear <name>,\n\nThank you for reaching out regarding your Canon PIXMA MG3620. I understand how frustrating persistent paper jams can be. Here are a few additional troubleshooting steps you might not have tried:\n\n1. Check for any small, hidden debris inside the printer.\n2. Ensure the paper type and size settings align with the paper you’re using.\n3. Try using a different batch/brand of paper.\n\nIf the issue persists, you might need to contact Canon Support directly for further assistance or servicing.\n\nBest regards,\nCustomer Support",
      "score": 0.743
    }
  ]
}

```

## Roadmap

* zaawansowany reranking wyników (LLM)
* system feedbacku użytkownika
* multi-language support
* monitoring jakości odpowiedzi AI

---

## License

Dominik Hofman &copy 2025-2026