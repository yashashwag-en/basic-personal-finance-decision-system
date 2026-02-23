import math

def analyze_budget(income, fixed_expenses, variable_expenses, savings_goal, annual_return=8):

    if income <= 0:
        return {"error": "Income must be greater than zero."}

    total_expenses = fixed_expenses + variable_expenses
    net_cashflow = income - total_expenses

    # Ratios
    fixed_ratio = fixed_expenses / income
    variable_ratio = variable_expenses / income
    savings_ratio = net_cashflow / income

    # 50/30/20 ideal values
    ideal_fixed = 0.5
    ideal_variable = 0.3
    ideal_savings = 0.2

    # Financial Stability Index (weighted scoring)
    score = 0

    # Cash flow component (40%)
    if net_cashflow > 0:
        score += 40 * min(savings_ratio / ideal_savings, 1)
    else:
        score += 0

    # Fixed cost efficiency (25%)
    score += 25 * max(0, 1 - abs(fixed_ratio - ideal_fixed))

    # Variable control (20%)
    score += 20 * max(0, 1 - abs(variable_ratio - ideal_variable))

    # Emergency readiness (15%)
    emergency_required = total_expenses * 6
    if net_cashflow > 0:
        months_to_emergency = emergency_required / net_cashflow
        if months_to_emergency <= 12:
            score += 15
        else:
            score += max(0, 15 - (months_to_emergency / 12))
    else:
        months_to_emergency = None

    score = round(min(score, 100), 2)

    # Risk assessment
    if savings_ratio < 0:
        risk = "Critical"
    elif savings_ratio < 0.1:
        risk = "High"
    elif savings_ratio < 0.2:
        risk = "Moderate"
    else:
        risk = "Low"

    # Emergency runway (if income stops)
    runway_months = income / total_expenses if total_expenses > 0 else math.inf

    # Goal projection with compounding
    monthly_return = annual_return / 100 / 12

    if net_cashflow > 0:
        if monthly_return > 0:
            months_to_goal = math.log(
                (savings_goal * monthly_return / net_cashflow) + 1
            ) / math.log(1 + monthly_return)
        else:
            months_to_goal = savings_goal / net_cashflow
    else:
        months_to_goal = None

    # Optimization Simulation (reduce variable expenses by 10%)
    optimized_variable = variable_expenses * 0.9
    optimized_cashflow = income - (fixed_expenses + optimized_variable)

    # Recommendations (strict financial logic)
    recommendations = []

    if net_cashflow < 0:
        recommendations.append("Your expenses exceed income. Immediate cost reduction required.")

    if fixed_ratio > 0.6:
        recommendations.append("Fixed commitments are high. Consider restructuring rent/EMIs.")

    if variable_ratio > 0.35:
        recommendations.append("Lifestyle spending exceeds healthy limits.")

    if savings_ratio < 0.2:
        recommendations.append("Increase savings to at least 20% of income.")

    if savings_ratio > 0.35:
        recommendations.append("Strong surplus detected. Consider diversified investments.")

    if runway_months < 3:
        recommendations.append("Emergency survival capacity is low (<3 months).")

    return {
        "net_cashflow": round(net_cashflow,2),
        "score": score,
        "risk": risk,
        "fixed_ratio": round(fixed_ratio*100,2),
        "variable_ratio": round(variable_ratio*100,2),
        "savings_ratio": round(savings_ratio*100,2),
        "emergency_required": round(emergency_required,2),
        "months_to_emergency": round(months_to_emergency,1) if months_to_emergency else None,
        "runway_months": round(runway_months,1),
        "months_to_goal": round(months_to_goal,1) if months_to_goal else None,
        "optimized_cashflow": round(optimized_cashflow,2),
        "recommendations": recommendations
    }