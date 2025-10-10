# Poetry AI Research Design Clarification
## Control Group vs Experimental Design Framework

---

## 🎯 **CORRECT Research Design Understanding**

### **Core Research Question:**
**How do AI parameter settings (structured vs exploratory) affect collaborative creative writing outcomes?**

### **Control Group Design:**
- **UNAWARE UI = CONTROL CONDITION** 
  - Participants don't know about parameter differences
  - Eliminates expectation/bias effects
  - Provides pure measure of AI parameter impact

- **AWARE UI = AWARENESS CHECK**
  - Tests whether knowledge of parameters affects behavior
  - Validates that observed differences are due to AI, not expectations

---

## 📊 **Room Function Clarification**

### **PRIMARY Research Data (Main Study):**
```
Room 2: Structured + Unaware    vs    Room 4: Exploratory + Unaware
        ↓                                     ↓
   CONTROL GROUP                        CONTROL GROUP
   (Pure parameter effects - no awareness bias)
   
   THIS IS THE MAIN RESEARCH COMPARISON
```

### **SECONDARY Data (Methodological Validation):**
```
Room 1: Structured + Aware      vs    Room 2: Structured + Unaware
Room 3: Exploratory + Aware     vs    Room 4: Exploratory + Unaware
        ↓                                     ↓
   AWARENESS CHECK                      CONTROL VALIDATION
   (Does knowing about parameters change behavior?)
```

---

## 🔬 **Research Hierarchy**

### **Priority 1: Main Research Questions**
1. **Parameter Effects on Collaboration** (Room 2 vs Room 4)
2. **Interaction Type Patterns** (Room 2 vs Room 4)
3. **Creative Output Differences** (Room 2 vs Room 4)
4. **Scaffolding Quality Variation** (Room 2 vs Room 4)

### **Priority 2: Methodological Validation**
5. **Awareness Bias Check** (Room 1 vs Room 2, Room 3 vs Room 4)
6. **Effect Consistency Validation** (Cross-condition analysis)

---

## 📈 **Analysis Strategy**

### **Primary Analysis:**
- **Independent t-tests**: Room 2 vs Room 4 comparisons
- **Effect sizes**: Cohen's d for parameter differences
- **Conversation analysis**: Unaware participant interactions only
- **Creative outcome measures**: Based on control group data

### **Secondary Analysis:**
- **Awareness impact**: Compare aware vs unaware within same parameters
- **Bias validation**: Ensure main findings aren't due to expectation effects
- **Interaction effects**: Parameter × Awareness (if significant bias detected)

---

## ✅ **Key Design Strengths**

### **Internal Validity:**
- ✅ **Unaware participants** eliminate expectation bias
- ✅ **Identical prompts** across all conditions
- ✅ **Parameter-only manipulation** in control groups
- ✅ **Awareness checks** validate finding authenticity

### **External Validity:**
- ✅ **Real-world conditions** (users typically unaware of AI parameters)
- ✅ **Ecological validity** (natural interaction without technical knowledge)
- ✅ **Practical implications** (findings apply to actual AI writing tools)

---

## 🎯 **Supervisor Communication Summary**

**"The research design uses unaware participants (Rooms 2 & 4) as the primary control condition to measure pure AI parameter effects on collaborative writing, with aware participants (Rooms 1 & 3) serving as methodological checks to ensure observed differences result from AI behavior rather than participant expectations. This approach provides robust internal validity while maintaining ecological validity for real-world AI writing tool applications."**

---

## 📋 **Implementation Priorities**

### **Development Focus:**
1. **Rooms 2 & 4** (control groups) - highest priority
2. **Data logging** for unaware conditions - critical
3. **Rooms 1 & 3** (awareness checks) - secondary priority
4. **Cross-condition analysis tools** - validation support

### **Testing Sequence:**
1. Validate Room 2 vs Room 4 parameter differences
2. Confirm unaware participant experience authenticity  
3. Test aware condition interfaces
4. Validate cross-condition comparison capabilities

**Status: Research design clarification documented and tracked** ✅