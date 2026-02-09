# ActReady AI - Automated Technical Documentation Generator
# Requirement: EU AI Act Annex IV (Technical Documentation)

from datetime import datetime
import json

class ActReadyReportGenerator:
    def __init__(self, system_name, version):
        self.system_name = system_name
        self.version = version
        self.report_date = datetime.now().strftime("%Y-%m-%d")

    def generate_annex_iv_template(self, model_metadata, risk_assessment):
        """Generates a structured report based on EU AI Act Annex IV."""
        
        report = {
            "header": {
                "organization": "ActReady AI Client",
                "system_name": self.system_name,
                "version": self.version,
                "date": self.report_date,
                "compliance_status": "DRAFT - FOR INTERNAL REVIEW"
            },
            "sections": {
                "1_general_description": {
                    "intended_purpose": model_metadata.get("purpose"),
                    "hardware_requirements": "AWS ml.m5.xlarge or higher",
                    "interactions": "REST API via Amazon API Gateway"
                },
                "2_development_process": {
                    "methods": "Supervised Learning / XGBoost",
                    "data_provenance": "S3 Encrypted Bucket (EU-Central-1)",
                    "labelling_process": "Automated SageMaker Ground Truth"
                },
                "3_monitoring_and_control": {
                    "human_oversight": "Human-in-the-loop dashboard enabled",
                    "drift_threshold": "0.05 (KS-Test)"
                },
                "4_risk_management": {
                    "identified_risks": risk_assessment.get("risks"),
                    "mitigation_steps": risk_assessment.get("mitigation")
                }
            }
        }
        
        filename = f"EU_AI_ACT_Technical_File_v{self.version}.json"
        with open(filename, "w") as f:
            json.dump(report, f, indent=4)
        
        print(f"✅ Success: {filename} generated.")

# Example Usage for your GitHub Demo
metadata = {"purpose": "Creditworthiness Assessment", "type": "High-Risk Annex III"}
risks = {
    "risks": ["Algorithmic Bias", "Data Poisoning"],
    "mitigation": ["SageMaker Clarify Bias Check", "KMS Encryption"]
}

generator = ActReadyReportGenerator("Financial-Predictor-X", "1.0.4")
generator.generate_annex_iv_template(metadata, risks)
