
timestamps {
	
	  println "=====> JOB: System-Full-Regression ..."	
	
	
	  lock("System-Regression-Full") {
	
	
	
	  stage('Deploy-Clean') {
	
		println "=====> STAGE: Deploy-Clean"
	
		def BRANCHES = [:]
	
		BRANCHES["Integrate"] = {
	
		  println "--> Calling JOB: System-Auto-Deploy (ete1, integrate, true, false) and waiting ..."
	
		  deployJob = build job: 'System-Auto-Deploy',
	
			parameters:[
	
			  string(name: 'LAB', value: 'ete1'),
	
			  string(name: 'DEPLOY', value: 'integrate'),
	
			  booleanParam(name: 'CONTENT_UPDATE', value: true),
	
			  booleanParam(name: 'PRODUCTION', value: false),
	
			  booleanParam(name: 'JAVA_PROFILER', value: false),
	
			  booleanParam(name: 'JACOCO', value: true)],
	
			propagate:true,
	
			wait:true
	if(deplyJob.getResult().toString().trim().equals("SUCCESS")) {
	
	println "--> Calling JOB: System-Auto-Clean (ccare1, 10.107.141.31, 10.107.138.116) and waiting ..."
	
    build job: 'System-Auto-Clean',
	
	parameters:[

	  string(name: 'DB_USER', value: 'ccare1'),

	  string(name: 'DB_IP', value: '10.107.141.31'),

	  string(name: 'SDP_IP', value: '10.107.138.116')],

	propagate:true,

	wait:true
	
	println "--> Calling JOB: EBI-Regression-Build (ete1, selfcare, ebimaster_integrate) ..."
	
    build job: 'EBI-Regression-Build',
	
parameters: [

	string(name: 'USER_EMAIL', value: "${EMAIL}"),

string(name: 'LAB', value: 'ete1'),

string(name: 'APPLICATION', value: 'selfcare'),

string(name: 'BRANCH', value: 'ebimaster_integrate'),

string(name: 'TESTSET', value: 'TS17'),

booleanParam(name: 'RERUN', value: true),

booleanParam(name: 'REPORT', value: true),

booleanParam(name: 'JACOCO', value: true)

],

propagate: false,

wait: true

println "--> Calling JOB: EBI-Regression-Build (ete1, customercare, ebimaster_integrate) ..."

  build job: 'EBI-Regression-Build',

parameters: [

	string(name: 'USER_EMAIL', value: "${EMAIL}"),

string(name: 'LAB', value: 'ete1'),

string(name: 'APPLICATION', value: 'customercare'),

string(name: 'BRANCH', value: 'ebimaster_integrate'),

string(name: 'TESTSET', value: 'TS16'),

booleanParam(name: 'RERUN', value: true),

booleanParam(name: 'REPORT', value: true),

booleanParam(name: 'JACOCO', value: true)

],

propagate: false,

wait: true

println "--> Calling JOB: EBI-Regression-Build (ete1, resellercare, ebimaster_integrate) ..."

  build job: 'EBI-Regression-Build',

parameters: [

	string(name: 'USER_EMAIL', value: "${EMAIL}"),

	string(name: 'LAB', value: 'ete1'),

	string(name: 'APPLICATION', value: 'resellercare'),

	string(name: 'BRANCH', value: 'ebimaster_integrate'),

	string(name: 'TESTSET', value: 'TS18'),

	booleanParam(name: 'RERUN', value: true),

	booleanParam(name: 'REPORT', value: true),

	booleanParam(name: 'JACOCO', value: true)

],

propagate: false,

wait: true


println "--> Calling JOB: EBI-Regression-Build (ete1, agw, ebimaster_integrate) ..."

	  build job: 'EBI-Regression-Build',

		parameters:[

		  string(name:'USER_EMAIL', value:"${EMAIL}"),

		  string(name:'LAB', value:'ete1'),

		  string(name: 'APPLICATION', value: 'agw'),

		  string(name: 'BRANCH', value: 'ebimaster_integrate'),

		  string(name: 'TESTSET', value: 'TS19'),

		  booleanParam(name: 'RERUN', value: true),

		  booleanParam(name: 'REPORT', value: true),

		  booleanParam(name: 'JACOCO', value: true)

		],

		propagate: false,

		wait: true
							
	

}

else {

	println "--> skipping ete1 regression"
}


		}
		

	
		BRANCHES["Release"] = {
	
		  println "--> Calling JOB: System-Auto-Deploy (etep, release, true, false) and waiting ..."
	
		  deployJobRelease = build job: 'System-Auto-Deploy',
	
			parameters:[
	
			  string(name: 'LAB', value: 'etep'),
	
			  string(name: 'DEPLOY', value: 'release'),
	
			  booleanParam(name: 'CONTENT_UPDATE', value: true),
	
			  booleanParam(name: 'PRODUCTION', value: false),
	
			  booleanParam(name: 'JAVA_PROFILER', value: false)],
	
			propagate:true,
	
			wait:true
	
			sleep (60)
			
 if(deplyJob.getResult().toString().trim().equals("SUCCESS")) {
		
	
		  println "--> Calling JOB: System-Auto-Clean (ccarep, 10.107.141.31, 10.107.138.131) and waiting ..."
	
		  build job: 'System-Auto-Clean',
	
			parameters:[
	
			  string(name: 'DB_USER', value: 'ccarep'),
	
			  string(name: 'DB_IP', value: '10.107.141.31'),
	
			  string(name: 'SDP_IP', value: '10.107.138.131')],
	
			propagate:true,
	
			wait:true

println "--> Calling JOB: EBI-Regression-Build (etep, selfcare, ebimaster_release) ..."

sc_build = build job: 'EBI-Regression-Build',

parameters: [

	string(name: 'USER_EMAIL', value: "${EMAIL}"),

string(name: 'LAB', value: 'etep'),

string(name: 'APPLICATION', value: 'selfcare'),

string(name: 'BRANCH', value: 'ebimaster_release'),

string(name: 'TESTSET', value: 'TS17'),

booleanParam(name: 'RERUN', value: true),

booleanParam(name: 'REPORT', value: true)

],

propagate: false,

wait: true


println "--> Calling JOB: EBI-Regression-Build (etep, customercare, ebimaster_release) ..."

cc_build = build job: 'EBI-Regression-Build',

parameters: [

	string(name: 'USER_EMAIL', value: "${EMAIL}"),

string(name: 'LAB', value: 'etep'),

string(name: 'APPLICATION', value: 'customercare'),

string(name: 'BRANCH', value: 'ebimaster_release'),

string(name: 'TESTSET', value: 'TS16'),

booleanParam(name: 'RERUN', value: true),

booleanParam(name: 'REPORT', value: true)

],

propagate: false,

wait: true


println "--> Calling JOB: EBI-Regression-Build (etep, resellercare, ebimaster_release) ..."

	rc_build = build job: 'EBI-Regression-Build',

	parameters: [

		string(name: 'USER_EMAIL', value: "${EMAIL}"),

		string(name: 'LAB', value: 'etep'),

		string(name: 'APPLICATION', value: 'resellercare'),

		string(name: 'BRANCH', value: 'ebimaster_release'),

		string(name: 'TESTSET', value: 'TS18'),

		booleanParam(name: 'RERUN', value: true),

		booleanParam(name: 'REPORT', value: true)

	],

	propagate: false,

	wait: true


	println "--> Calling JOB: EBI-Regression-Build (etep, agw, ebimaster_release) ..."
	
			agw_build = build job: 'EBI-Regression-Build',
	
			parameters:[
	
			  string(name:'USER_EMAIL', value:"${EMAIL}"),
	
			  string(name:'LAB', value:'etep'),
	
			  string(name: 'APPLICATION', value: 'agw'),
	
			  string(name: 'BRANCH', value: 'ebimaster_release'),
	
			  string(name: 'TESTSET', value: 'TS19'),
	
			  booleanParam(name: 'RERUN', value: true),
	
			  booleanParam(name: 'REPORT', value: true)
	
			  ],
	
			propagate: false,
	
			wait: true
	




	}
	
	else {

	println "--> skipping etep regression"
    }
	
		}
	
		println "\n--> Starting parallel jobs System-Auto-Deploy and System-Auto-Clean ...\n"
	
		parallel BRANCHES
	
		sleep(10)
	
	  }
	
	
	
	
	
	  stage('Phase 3') {
	
		println "=====> STAGE: PHASE 3"
	
		/*println "--> Calling JOB: EBI-Regression-Build (ete1, gy, ebimaster_integrate) ..."
	
		build job: 'EBI-Regression-Build',
	
		  parameters:[
	
			string(name:'USER_EMAIL', value:"${EMAIL}"),
	
			string(name:'LAB', value:'ete1'),
	
			string(name: 'APPLICATION', value: 'gy'),
	
			string(name: 'BRANCH', value: 'ebimaster_integrate'),
	
			string(name: 'TESTSET', value: 'TS94'),
	
			booleanParam(name: 'RERUN', value: true),
	
			booleanParam(name: 'REPORT', value: true)
	
		  ],
	
		  propagate: false,
	
		  wait: true
	
		sleep(10)
	
		*/
	
		println "--> Calling JOB: EBI-Regression-Build (ete1, ro, ebimaster_integrate) ..."
	
		build job: 'EBI-Regression-Build',
	
		  parameters:[
	
			string(name:'USER_EMAIL', value:"${EMAIL}"),
	
			string(name:'LAB', value:'ete1'),
	
			string(name: 'APPLICATION', value: 'ro'),
	
			string(name: 'BRANCH', value: 'ebimaster_integrate'),
	
			string(name: 'TESTSET', value: 'TS93'),
	
			booleanParam(name: 'RERUN', value: true),
	
			booleanParam(name: 'REPORT', value: true)
	
		  ],
	
		  propagate: false,
	
		  wait: true
	
		/* sleep(10)
	
		println "--> Skipping ETE-1 VoLTE MI until 100% failures are resolved"
	
		println "--> Calling JOB: EBI-Regression-Build (ete1, volte, ebimaster_integrate) ..."
	
		build job: 'EBI-Regression-Build',
	
		  parameters:[
	
			string(name:'USER_EMAIL', value:"${EMAIL}"),
	
			string(name:'LAB', value:'ete1'),
	
			string(name: 'APPLICATION', value: 'volte'),
	
			string(name: 'BRANCH', value: 'ebimaster_integrate'),
	
			string(name: 'TESTSET', value: 'TS92'),
	
			booleanParam(name: 'RERUN', value: true),
	
			booleanParam(name: 'REPORT', value: true)
	
		  ],
	
		  propagate: false,
	
		  wait: true
	
		  */
	
	  }
	
	 
	
	
	
	//   stage('Jacoco'){
	
	//     println "--> Calling JOB: EBI-Jacoco-Build (ete1, webrc, integrate) ..."
	
	//     build job: 'EBI-Jacoco-Build',
	
	//       parameters:[
	
	//         string(name:'APP', value:'webrc'),
	
	//         string(name: 'LAB', value: 'ete1'),
	
	//         string(name: 'BRANCH', value: 'integrate'),
	
	//         string(name: 'BUILD', value: rc_build.getNumber().toString().trim())
	
	//       ],
	
	//       propagate: false,
	
	//       wait: true
	
	//       sleep(5)
	
	//       println "--> Calling JOB: EBI-Jacoco-Build (ete1, webcc, integrate) ..."
	
	//     build job: 'EBI-Jacoco-Build',
	
	//       parameters:[
	
	//         string(name:'APP', value:'webcc'),
	
	//         string(name: 'LAB', value: 'ete1'),
	
	//         string(name: 'BRANCH', value: 'integrate'),
	
	//         string(name: 'BUILD', value: cc_build.getNumber().toString().trim())
	
	//       ],
	
	//       propagate: false,
	
	//       wait: true
	
	//       sleep(5)
	
	//       println "--> Calling JOB: EBI-Jacoco-Build (ete1, websc, integrate) ..."
	
	//     build job: 'EBI-Jacoco-Build',
	
	//       parameters:[
	
	//         string(name:'APP', value:'websc'),
	
	//         string(name: 'LAB', value: 'ete1'),
	
	//         string(name: 'BRANCH', value: 'integrate'),
	
	//         string(name: 'BUILD', value: sc_build.getNumber().toString().trim())
	
	//       ],
	
	//       propagate: false,
	
	//       wait: true
	
	//       sleep(5)
	
	//       println "--> Calling JOB: EBI-Jacoco-Build (ete1, agw, integrate) ..."
	
	//     build job: 'EBI-Jacoco-Build',
	
	//       parameters:[
	
	//         string(name:'APP', value:'agw'),
	
	//         string(name: 'LAB', value: 'ete1'),
	
	//         string(name: 'BRANCH', value: 'integrate'),
	
	//         string(name: 'BUILD', value: agw_build.getNumber().toString().trim())
	
	//       ],
	
	//       propagate: false,
	
	//       wait: true
	
	//   }
	
	
	
	  stage('Finish') {
	
		println "=====> STAGE: FINISH"
	
	  }
	
	
	
	  } // lock
	
	}
	

