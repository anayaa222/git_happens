Hospital backend folder is a work in progress idea that we could not implement due to time constraints. We thought of adding it onto our developed project as something new to explore.

please refer to the tricorp frontend for the hackathon statement answer.






## **Title Slide**

**Smart Healthcare UI/UX System**
**Symptom-Based Risk Analysis & Queue Optimization**

* Your Name
* BTech (2nd Year)
* Domain: Web Dev + AI/UX
* Date

---

## **Real-World Problem**

Hospitals today face a **critical inefficiency at entry level**:

* Patients are treated on **first-come-first-serve basis**
* No immediate **risk prioritization mechanism**
* Emergency cases may **wait behind non-critical cases**

### 🔴 Result:

* Delayed treatment for serious patients
* Panic & overcrowding
* Staff overwhelmed at reception

---

## **Core Idea**

A **self-service UI system** that:

* Takes **1 primary symptom input**
* Dynamically connects it to **related symptoms**
* Performs **risk analysis (NOT diagnosis)**
* Assigns:

  * **Risk Score (0–100)**
  * **Priority Category (A/B/C)**

👉 Goal: **Sort patients BEFORE they reach staff**

---

## **Key Design Philosophy**

This system is built on 3 principles:

### 1. **Speed**

* Takes less than **30 seconds per patient**

### 2. **Simplicity**

* No typing-heavy forms
* Click-based interaction

### 3. **Non-Intrusive**

* No personal data collected
* Only **symptom-based logic**

---

## **User Flow (Step-by-Step)**

1. Patient selects **primary symptom**
2. System displays **related symptoms dynamically**
3. Patient selects additional symptoms
4. System runs **risk scoring algorithm**
5. Output generated:

   * Score (0–100)
   * Category (A/B/C)
   * Patient Token ID
6. Patient directed to **assigned queue**

---

## **Symptom Mapping System**

The backend uses a **symptom relationship model**:

Example:

| Primary Symptom | Related Symptoms          |
| --------------- | ------------------------- |
| Fever           | Chills, Sweating, Fatigue |
| Chest Pain      | Breathlessness, Arm Pain  |
| Headache        | Nausea, Dizziness         |

👉 This creates a **symptom network**, not isolated inputs.

---

## ** Risk Analysis Logic (Important Slide)**

The system assigns weights to symptoms:

* Mild symptoms → Low score
* Severe symptoms → High score
* Dangerous combinations → Extra weight

### Example:

* Fever → +20
* Chest Pain → +40
* Breathlessness → +30

👉 Combined → **Higher risk amplification**

---

## **Slide 8: Risk Score Formula (Conceptual)**

```
Risk Score = Base Symptom Weight 
           + Related Symptoms Weight 
           + Combination Risk Bonus (tentative)
```

### Key Factors:

* Severity
* Number of symptoms
* Critical combinations

👉 Final Score capped at **100**

---

## **Risk Categorization System**

| Score Range | Category | Meaning     |
| ----------- | -------- | ----------- |
| 0 – 35      | C        | Low Risk    |
| 35 – 65     | B        | Medium Risk |
| 65 – 100    | A        | High Risk   |

---

## **Output Screen (UI Concept)**

System displays:

* ✅ Patient Token Number
* 📊 Risk Score (e.g., 72/100)
* 🚨 Category: **A (High Priority)**

👉 No diagnosis shown
👉 Only **priority classification**

---

## **Nurse Allocation Logic**

Instead of one queue:

### 🟥 Category A → Emergency Nurses

* Immediate attention
* Critical cases

### 🟧 Category B → Moderate Care

* Needs attention but not urgent

### 🟩 Category C → General Queue

* Routine cases

👉 This reduces **bottleneck at reception**

---

## **UI/UX Design Decisions**

* Large clickable buttons (touch-friendly)
* Minimal reading required
* Color coding:

  * Red → High risk
  * Orange → Medium
  * Green → Low
* Step-by-step guided flow

👉 Designed for **all age groups**

---

## **Why No Personal Data?**

* Faster interaction
* Privacy-friendly
* Avoids delays in emergency
* Data handled later by nurse

👉 Focus = **triage, not registration**

---

## **System Architecture (Simple)**

**Frontend:**

* HTML, CSS, JavaScript

**Logic Layer:**

* Symptom mapping
* Risk calculation

**Output Layer:**

* Score + Category + Token

(Optional future backend integration)

---

## **Real-Life Example**

### Patient Input:

* Primary: Chest Pain
* Selected: Breathlessness, Sweating

### System Analysis:

* Chest Pain → 40
* Breathlessness → 30
* Sweating → 10
* Combo Bonus → +10

👉 **Total Score = 90 → Category A**

---

## ** Benefits**

### 🏥 For Hospitals:

* Better patient flow
* Efficient nurse allocation

### 👨‍⚕️ For Staff:

* Reduced decision pressure
* Faster triage

### 🧑‍🤝‍🧑 For Patients:

* Less waiting
* Faster critical care

---

## **Limitations**

* Not a medical diagnosis system

* Depends on:

  * User honesty
  * Correct symptom selection

* Requires:

  * Proper medical validation of weights

---

future scope: 
* AI-based prediction model
* Integration with hospital systems
* Voice-based symptom input
* Mobile app version
* Real-time dashboard for doctors

---

**What makes this different?**
* Combines:

  * UI/UX + Healthcare
  * Rule-based AI logic
* Focus on **triage optimization**
* Scalable for:

  * Hospitals
  * Clinics
  * Emergency setups

---



* Small UI innovation → **Huge operational impact**
* Solves:

  * Waiting time
  * Panic
  * Mismanagement

👉 Focus:
**Analyze → Categorize → Prioritize**
