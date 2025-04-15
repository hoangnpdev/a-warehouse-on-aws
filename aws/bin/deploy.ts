#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { ProdStack } from '../warehouse/prod-stack';

const app = new cdk.App();
new ProdStack(app, 'prodEnvironment', {
    // env: {account: '833478914346', region: 'us-west-2'}
});