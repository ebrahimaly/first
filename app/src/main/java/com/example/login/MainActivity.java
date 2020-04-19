package com.example.login;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    TextView reg;
    EditText edemail,edpass;
    Button login;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        reg=findViewById(R.id.reg);
        edemail=findViewById(R.id.email);
        edpass=findViewById(R.id.pass);
        login=findViewById(R.id.login);
        login.setOnClickListener(this);
        reg.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        if(v==reg) {
            Intent regist = new Intent(this, Main2Activity.class);
            startActivity(regist);
        }else if (v==login){

        }
    }
}
