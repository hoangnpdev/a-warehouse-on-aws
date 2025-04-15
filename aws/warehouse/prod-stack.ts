import * as cdk from 'aws-cdk-lib';
import {Construct} from 'constructs';
import {HadoopConstruct} from "./hadoop-construct";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import {IpAddresses} from "aws-cdk-lib/aws-ec2";

export class ProdStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    new ec2.Vpc(this, 'internal_network', {
      ipAddresses: IpAddresses.cidr('192.168.0.0/16'),
      availabilityZones: [CLUSTER_INFO.MAIN_AZ],
      subnetConfiguration: [
        {
          name: 'private_subnet',
          subnetType: ec2.SubnetType.PRIVATE_ISOLATED
        }
      ]
    });

    new HadoopConstruct(this, 'hadoop_cluster');

    new cdk.CfnOutput(this, 'deploy_formation', {
      value: "nothing",
    })
  }
}
