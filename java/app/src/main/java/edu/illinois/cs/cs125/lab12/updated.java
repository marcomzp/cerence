package edu.illinois.cs.cs125.lab12;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;

public class updated extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.updated);
        ImageView logoPic = findViewById(R.id.logo);
        logoPic.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(updated.this, MainActivity.class);
                startActivity(intent);

            }
        });
    }
}
