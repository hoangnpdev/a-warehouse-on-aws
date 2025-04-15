import {Construct} from "constructs";
import {aws_ec2, aws_emr, aws_iam} from "aws-cdk-lib";

export class HadoopConstruct extends Construct {
    constructor(scope: Construct, id: string) {
        super(scope, id);
        // role
        let emrServiceRole = new aws_iam.Role(this, "EmrServiceRole", {
            assumedBy: new aws_iam.ServicePrincipal("elasticmapreduce.amazonaws.com"),
        });
        emrServiceRole.addManagedPolicy(aws_iam.ManagedPolicy.fromAwsManagedPolicyName("AmazonEMRServicePolicy_v2 "));
        let emrServiceInstanceRole = new aws_iam.Role(this, "EmrServiceInstanceRole", {
            assumedBy: new aws_iam.ServicePrincipal("ec2.amazonaws.com")
        });
        emrServiceInstanceRole.addManagedPolicy(aws_iam.ManagedPolicy.fromAwsManagedPolicyName("AmazonElasticMapReduceforEC2Role"));
        new aws_emr.CfnCluster(this, id,  {
            serviceRole: "EmrServiceRole",
            jobFlowRole: "EmrServiceInstanceRole",
            name: "hadoop-cluster",
            instances: {
                ec2SubnetId: "private_subnet",
                masterInstanceGroup: {
                    instanceCount: 1,
                    instanceType: aws_ec2.InstanceClass.T4G,
                    ebsConfiguration: {
                        ebsBlockDeviceConfigs: [
                            {
                                volumeSpecification: {
                                    sizeInGb: 1024,
                                    volumeType: aws_ec2.EbsDeviceVolumeType.GP3
                                },
                                volumesPerInstance: 3
                            }
                        ]
                    }
                },
                coreInstanceGroup: {
                    instanceCount: 5,
                    instanceType: aws_ec2.InstanceClass.T4G,
                    ebsConfiguration: {
                        ebsBlockDeviceConfigs: [

                        ]
                    }
                },
            },
            applications: [
                { name: "Spark" },
                { name: "Hadoop" },
                { name: "JupyterHub" },
            ]
        });

    }
}