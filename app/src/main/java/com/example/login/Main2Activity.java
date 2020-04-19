package com.example.login;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class Main2Activity extends AppCompatActivity {
    EditText em,ps,na,cps;
    Button rg;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        na=findViewById(R.id.name);
        em=findViewById(R.id.email1);
        ps=findViewById(R.id.pass1);
        cps=findViewById(R.id.cpass);
        rg=findViewById(R.id.rg);
        rg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String name=na.getText().toString();
                String email=em.getText().toString();
                String pass=ps.getText().toString();
                String cpass=cps.getText().toString();
                if(name.equals("")){
                    Toast.makeText(Main2Activity.this, "name required", Toast.LENGTH_SHORT).show();
                }
               else if(email.equals("")){
                    Toast.makeText(Main2Activity.this, "email required", Toast.LENGTH_SHORT).show();
                }
                else if(pass.equals("")){
                    Toast.makeText(Main2Activity.this, "password required", Toast.LENGTH_SHORT).show();
                }
                else if(cpass.equals("")){
                    Toast.makeText(Main2Activity.this, "confirm password required", Toast.LENGTH_SHORT).show();
                }else if (!cpass.equals("pass")){
                    Toast.makeText(Main2Activity.this, "confirm password mismitch", Toast.LENGTH_SHORT).show();

                }


            }
        });
    }
}
