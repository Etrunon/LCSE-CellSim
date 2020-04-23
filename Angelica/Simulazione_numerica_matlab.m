clear
clc
close all

N0 = 25;
num_gen = 20;
num_simul = 10000;
d = 0.45; %probabilità di morte
D = zeros(num_simul, num_gen);

%% Simulazione
for ii=1:num_simul
    D(ii,1)=N0;
    for jj=1:(num_gen-1)
        D(ii,jj+1)= D(ii,jj);
        for kk=1:D(ii,jj)
            moneta = rand();
                if moneta<d
                    D(ii,jj+1)=D(ii,jj+1)-1;
                end
        end
        D(ii,jj+1)=2*D(ii,jj+1);
    end
end

%% Plot evoluzione temporale (tante generazioni)
x=0:(num_gen-1);

time_evol = figure();

for ll=1:num_simul
    plot(x, D(ll,:), 'LineStyle', ':', 'Marker', '.', 'MarkerSize', 3)
    hold on
end

mean_D=zeros(1,num_gen);
for ll=1:num_gen
    mean_D(ll)=mean(D(:,ll));
end
plot(x, mean_D, 'LineStyle', 'none', 'Marker', 'x', 'MarkerSize', 6)

hold off

%% Plot binomiale (una generazione)
x=0:2:(2*N0);
y=zeros(1, N0+1);

for mm=1:num_simul
    y(1, D(mm,2)/2+1)=y(1, D(mm,2)/2+1)+1;
end

y_binom = zeros(1, N0+1);
for ii=1:N0+1 
    y_binom(ii) = nchoosek(N0, ii-1)*(1-d)^(ii-1) * (d)^(N0 - ii+1);
end

b = N0*(1-d);
c = sqrt(N0*d*(1-d));
a = 1 / (c*sqrt(2*pi));

binom = figure();

plot(x, y/num_simul, 'LineStyle', ':', 'Marker', '.', 'MarkerSize', 3)
hold on
plot(x, y_binom, 'LineStyle', '-.', 'Marker', 'o', 'MarkerSize', 3)
hold on
tmp = 0:0.1:2*N0;
plot(tmp, a*exp(-0.5*((tmp./2-b*ones(size(tmp)))/c).^2), 'Color', 'k')

hold off