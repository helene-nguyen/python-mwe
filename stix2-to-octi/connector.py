class Connector:
    def __init__(self, config, helper):
        # Load configuration file and connection helper
        self.config = config
        self.helper = helper

    def process_message(self):
        friendly_name = f"Connector runs"
        work_id = self.helper.api.work.initiate_work(
            self.config.connector.id, friendly_name
        )

        # Add object
        stix_objects_bundle = self.helper.stix2_create_bundle(

        )

        bundle_sent = self.helper.send_stix2_bundle(
            stix_objects_bundle,
            work_id=work_id
        )

        length_bundle_sent = len(bundle_sent)
        self.helper.connector_logger.info(
            "[CONNECTOR] Sending STIX objects to OpenCTI...",
            {"length_bundle_sent": length_bundle_sent},
        )

        message = "ServiceNow - Finished work"
        self.helper.api.work.to_processed(work_id, message)

    def run(self):
        self.helper.schedule_process(
            message_callback=self.process_message,
            duration_period=self.config.connector.duration_period.total_seconds(),
        )